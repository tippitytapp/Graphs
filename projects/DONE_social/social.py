import random
import time
from utils import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
        return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")
        # Create friendships
        possible_friendsships = []
        for user_id in self.users:
            for friend_id in range(user_id +1, self.last_id + 1):
                possible_friendsships.append((user_id, friend_id))

        # shuffle the possible friendships
        random.shuffle(possible_friendsships)

        # add friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendsships[i]
            self.add_friendship(friendship[0], friendship[1])
    
    def  populate_graph2(self, num_users, avg_friendships):
        # reset the graph
        self.reset()

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions +=1

        print(f"Collisions {collisions}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # visited = {}  # Note that this is a dictionary, not a set
        # # !!!! IMPLEMENT ME
        # q = Queue()
        # # enqueue the first user
        # q.enqueue([user_id])
        # # while the queue has something in it
        # while q.size() > 0:
        #     # create a path starting with the first thing in the queue
        #     path = q.dequeue()
        #     user = path[-1]
        #     if user not in visited:
        #         visited[user] = path
        #         for next_user in self.friendships[user]:
        #             new_path = list(path)
        #             new_path.append(next_user)
        #             q.enqueue(new_path)        
        # return visited
        '''This is the code BEEJ made in class'''
        q = Queue()
        # visited = set()
        # result = {}
        visited = {}
        q.enqueue([user_id]) # make this a list
        while q.size() > 0:
            path = q.dequeue()
            u = path[-1]
            if u not in visited:
                # visited.add(u)
                # result[u] = path
                visited[u] = path
                for neighbor in self.friendships[u]:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
        # return result
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    num_users = 10
    avg_friendships = 2
    # start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    # end_time = time.time()
    # print(f"O(n^2) runtime {end_time - start_time}")
    # startstart = time.time()
    # sg.populate_graph2(num_users, avg_friendships)
    # endend = time.time()
    # print(f"O(n) runtime {endend - startstart}")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

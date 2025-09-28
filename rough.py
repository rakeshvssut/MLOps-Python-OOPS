from oops_proj import chatbook


# lst = [1, 2, 3, 4, 5]

# ai = len(lst)
# print(ai)

# # method
# user1 = chatbook()
# user1.send_msg()

# user1 = chatbook()
# # print(user1._chatbook__name)

# print(user1.id)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)


# Using static method directly from class rather than object
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

# # getter and setter
# print(user1.get_name())

# # setter
# user1.set_name("Agent Vinod")

# print(user1.get_name())

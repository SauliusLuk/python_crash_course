# messages = ['Hey there!', 'Hello', 'Welcome']
# sent_messages = []
#
# while messages:
#     sent_message = messages.pop()
#     print(f"sending message '{sent_message}'")
#     sent_messages.append(sent_message)
#
# print("The following messages have been sent:")
# for message in sent_messages:
#     print(message)



def show_messages(messages):
    for message in messages:
        print(message)

def show_sent_messages(messages):
    sent_messages = []

    while messages:
        sent_message = messages.pop()
        sent_message_txt = f'Sent the message "{sent_message}"'
        sent_messages.append(sent_message_txt)

    for sent_message_txt in sent_messages:
        messages.append(sent_message_txt)


print("Original messages")
messages = ['Hey there!', 'Hello', 'Welcome']
show_messages(messages)

print("\nSent messages")
show_sent_messages(messages)
show_messages(messages)

"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts
    izzy = User('izzy')
    show = User('cmcconversations')
    users = [izzy, show]
    p1 = Tweet('cmcconversations', 'New episode drops Friday! #CMCConversations #Podcast')
    p2 = Tweet('izzy', 'Had the best guest in the studio today #BehindTheMic')
    p3 = Tweet('cmcconversations', 'Who should we interview next? Reply below!')
    posts = [p1, p2, p3]
    show.follow()
    show.follow()
    izzy.follow()
    show.unfollow()
    p1.like()
    p1.like()
    p2.like()
    p1.unlike()
    return users, posts


def main():
    # Call build_feed and display the returned objects and hashtags.
    users, posts = build_feed()

    print('Accounts:')
    for user in users:
        print(user)

    print('Posts:')
    for post in posts:
        print(post)
        print(post.hashtags())


if __name__ == '__main__':
    main()

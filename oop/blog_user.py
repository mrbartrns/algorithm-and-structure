class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        self.date = date
        self.content = content

    def __str__(self):
        return f"게시일: {self.date}\n내용: {self.content}"


class BlogUser:
    def __init__(self, name: str):
        """

        @param name: user name, type str
        @param posts: user's posts, type list
        """
        self.name = name
        self.posts = []

    # 게시글 인스턴스를 추가하기 위해서는 함수에 date, content를 입력받아야 한다.
    def add_post(self, date: str, content: str):
        self.posts.append(Post(date, content))

    def show_all_posts(self):
        size = len(self.posts)
        for i in range(size):
            post = self.posts[i]
            print(post)

    def __str__(self):
        return f"안녕하세요 {self.name}입니다.\n"


# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()

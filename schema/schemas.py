def serialize(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "likes": blog["likes"],
        "dislikes": blog["dislikes"],
        "content": blog["content"],
        "comments": blog.get("comments", []),
    }


def list_serial(blogs) -> list:
    return [serialize(blog) for blog in blogs]

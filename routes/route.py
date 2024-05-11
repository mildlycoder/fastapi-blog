from fastapi import APIRouter
from models.blogs import Blog

from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET Request
@router.get("/")
async def get_blogs():
    todos = list_serial(collection_name.find())
    return todos


# POST Request - add a blog
@router.post("/post-blog")
async def post_blog(blog: Blog):
    collection_name.insert_one(dict(blog))
    return {"message": "blog posted successfully"}


# PUT Request - like a blog
@router.put("/like-blog/{id}")
async def like_blog(id: str, blog: Blog):
    blog = collection_name.find_one({"_id": ObjectId(id)})

    if blog:
        curr_likes = blog.get("likes", 0)
        new_likes = curr_likes + 1

        collection_name.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": {"likes": new_likes}}
        )
        return {"message": "blog like successfully!"}
    else:
        return {"message": f"blog not found with {id} not found"}


# PUT Request - like a blog
@router.put("/dislike-blog/{id}")
async def dislike_blog(id: str, blog: Blog):
    blog = collection_name.find_one({"_id": ObjectId(id)})

    if blog:
        curr_dislikes = blog.get("dislikes", 0)
        new_dislikes = curr_dislikes + 1

        collection_name.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": {"dislikes": new_dislikes}}
        )
        return {"message": "blog disliked successfully"}
    else:
        return {"message": f"blog not found with {id} not found"}


# PUT Request - comment on blog
@router.put("/comment-blog/{id}")
async def comment(id: str, comment: str, blog: Blog):
    # Assuming `collection_name` is your MongoDB collection
    blog = collection_name.find_one({"_id": ObjectId(id)})

    if blog:
        curr_comments = blog.get("comments", [])
        curr_comments.append(comment)  # Append the new comment
        collection_name.update_one(
            {"_id": ObjectId(id)}, {"$set": {"comments": curr_comments}}
        )
        return {"message": "Comment added successfully"}
    else:
        return {"message": f"blog not found with {id} not found"}


@router.delete("/delete-blog/{id}")
async def delete_blog(id: str, blog: Blog):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": f"blog with {id} deleted successfully"}

import asyncio
import uvloop
import asyncpraw
import os
from dotenv import load_dotenv

load_dotenv()

Reddit_ID = os.getenv("Reddit_ID")
Reddit_Secret = os.getenv("Reddit_Secret")

# Note that these are coroutines, not regular methods
class getResources():
    def __init__(self):
        self.self = self
        
    async def get_sub_posts(self, subreddit):
        async with asyncpraw.Reddit(
            client_id=Reddit_ID,
            client_secret=Reddit_Secret,
            user_agent="hana-v0.1.0 (by /u/No767)",
        ) as redditapi:
            if "r/" in subreddit:
                subParser = subreddit.split("/")
                sub = subParser[1]
            else:
                sub = subreddit
            mainSub = await redditapi.subreddit(sub)
            async for submission in mainSub.new(limit=25):
                await submission.author.load()
                
    async def get_post(self, post_id: str):
        async with asyncpraw.Reddit(client_id=Reddit_ID, client_secret=Reddit_Secret, user_agent="hana-v0.1.0 (by /u/No767)") as redditapi:
            post = await redditapi.submission(id=post_id)
            await post.author.load()
            mainDict = {}
            for _ in range(11):
                mainDict["comments_number"] = post.num_comments
                mainDict["author"] = post.author.name
                mainDict["created_utc"] = post.created_utc
                mainDict["title"] = post.title
                mainDict["selftext"] = post.selftext
                mainDict["locked"] = post.locked
                mainDict["score"] = post.score
                mainDict["over_18"] = post.over_18
                mainDict["link_flair_text"] = post.link_flair_text
                mainDict["id"] = post.id
                mainDict["url"] = post.url
            return mainDict
            
            



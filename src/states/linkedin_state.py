from typing import TypedDict, List, Optional
from pydantic import BaseModel, Field

class LinkedInPost(BaseModel):
    topic: str
    linkedin_post: str = Field(description="The generated LinkedIn post content")
    news_sources: List[str] = Field(description="List of 3 source URLs")
    image_suggestion: Optional[str] = Field(description="Suggested image URL or null")

class LinkedInState(TypedDict):
    topic: str
    news_sources: List[str]
    linkedin_post: str
    image_suggestion: Optional[str]

class BlogRequest(BaseModel):
    topic: str


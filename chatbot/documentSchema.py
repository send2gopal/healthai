from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import List, Optional

class WorkExperience(BaseModel):
    company_name: Optional[str] = Field(description="Name of the company")
    position_name: Optional[str] = Field(description="Name of the position held")
    position_timeline: Optional[str] = Field(description="Duration of the position held")
    work_summary_keywords: List[str] = Field(description="Work Summary of a candidate summarized in the form of important keywords")

class ProjectExperience(BaseModel):
    company_name: Optional[str] = Field(description="Name of the company associated with the project")
    project_name: Optional[str] = Field(description="Name of the project")
    project_timeline: Optional[str] = Field(description="Duration of the project")
    project_work_summary_keywords: List[str] = Field(description="Project work summary summarized in the form of important keywords")

class Education(BaseModel):
    institution_name: Optional[str] = Field(description="Name of the educational institution")
    degree: Optional[str] = Field(description="Degree obtained")
    field_of_study: Optional[str] = Field(description="Field of study")
    start_year: Optional[int] = Field(description="Start year of the education")
    end_year: Optional[int] = Field(description="End year of the education")
    grade: Optional[str] = Field(description="Grade obtained")
    activities_and_societies: Optional[str] = Field(description="Activities and societies participated in")
    description: Optional[str] = Field(description="Additional details about the education")

class Candidate(BaseModel):
    #candidate_id: Optional[str] = Field(description="Unique identifier for the candidate")
    candidate_name: Optional[str] = Field(description="Name of the candidate")
    candidate_email: Optional[str] = Field(description="Email address of the candidate")
    candidate_phone_number: Optional[str] = Field(description="Phone number of the candidate")
    candidate_current_location: Optional[str] = Field(description="Current location of the candidate")
    candidate_languages: List[str] = Field(description="Languages spoken by the candidate")
    candidate_education: List[Education] = Field(description="Educational background of the candidate")
    candidate_skills: List[str] = Field(description="Skills possessed by the candidate")
    candidate_current_company: Optional[str] = Field(description="Current company of the candidate")
    candidate_past_company: List[str] = Field(description="Past companies the candidate has worked at")
    candidate_work_exp: List[WorkExperience] = Field(description="Work experience details of the candidate")
    candidate_project_exp: List[ProjectExperience] = Field(description="Project experience details of the candidate")
    candidate_links: List[str] = Field(description="Relevant links related to the candidate")
    candidate_total_exp: Optional[int] = Field(description="Total years of experience")
    candidate_current_ctc: Optional[float] = Field(description="Current CTC of the candidate")
    candidate_authenticity_score: Optional[float] = Field(description="Authenticity score of the candidate's profile")
    times_candidate_successfully_hired: Optional[int] = Field(description="Number of times the candidate has been successfully hired")
from mcp.server.fastmcp import FastMCP
from pydantic import Field, BaseModel

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}




# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc

@mcp.tool(
      name = "read_doc_content",
      description="Read the content of a document and return it as a string"
      )
def read_document(
        doc_id: str = Field(description = "Id of the document to read")
        ) :
    if doc_id not in docs:
         return ValueError(f"document {doc_id} not found in the list of document")
    return docs[doc_id]


@mcp.tool(
      name = "read_doc_content",
      description="Read the content of a document and return it as a string"
      )
def read_document(
        doc_id: str = Field(description = "Id of the document to read")
        ) -> str:
    if doc_id not in docs:
         return ValueError(f"document {doc_id} not found in the list of document")
    return docs[doc_id]

@mcp.tool(
      name = "edit_doc_content",
      description="Edit the document with the content passed in to this function"
      )
def edit_document(
        doc_id: str = Field(description = "Id of the document to edit"),
        old_string: str = Field(description="The text to replace. Must be exactly, including the white space"),
        new_Str: str = Field(description="the new text to insert in place of the old text")
        ) -> str:
    if doc_id not in docs:
         return ValueError(f"document {doc_id} not found in the list of document")

    docs[doc_id] = docs[doc_id].replace(old_string, new_Str)
    return 





if __name__ == "__main__":
    mcp.run(transport="stdio")
    
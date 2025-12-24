from pydantic import BaseModel


class CustomerRequest(BaseModel):
    customer_number: str

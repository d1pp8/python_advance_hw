import json
from pydantic import BaseModel, Field, EmailStr, model_validator, field_validator


class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)

class User(BaseModel):
    name: str = Field(min_length=2, pattern=r"^[A-Za-z\s]+$")
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    is_employed: bool = False
    address: Address


    @model_validator(mode='after')
    def check_user_employment(self):
        if self.is_employed and not (18 <= self.age <= 65):
            raise ValueError("User must be between 18 and 65 years old to be employed")
        return self


def process_user_json(json_data):

    for item in json_data:
        try:
            user = User.model_validate(item)
            json_output = user.model_dump_json(indent=4)
            print("\n✅ Valid JSON:")
            print(json_output)

        except Exception as e:
            print(f"\n❌ Validation error for user:")
            print(f"Name: {item.get('name')}")
            print(f"Age: {item.get('age')}")
            print(f"Employed: {item.get('is_employed')}")
            print(e)

def get_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    json_data = get_data()
    process_user_json(json_data)
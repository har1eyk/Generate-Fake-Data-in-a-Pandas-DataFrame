# Generate Fake Data in a Pandas DataFrame
I needed to generate fake data for a Pandas DataFrame for project. Specifically, I needed a fake name, email address and a number. I found two ways to create this and thought I would share here and help my future self so I don't forget. [Faker](https://github.com/joke2k/faker) is a great Python package for accomplishing this. 

## Faker
Import Faker

    from faker import Faker
    fake = Faker()

## Output
Output appears like this:

|   |       Name        |           Email            | Duration |
|---|-------------------|----------------------------|----------|
| 0 | Joshua Ortiz      | patrickpatrick@taylor.info |       53 |
| 1 | Brenda Chavez     | tking@hotmail.com          |        7 |
| 2 | Stephanie Johnson | reginald43@hotmail.com     |       26 |
| 3 | Whitney Santiago  | scott30@yahoo.com          |       38 |

*Table 1: Dataframe Output for Pandas DataFrame using Faker.*


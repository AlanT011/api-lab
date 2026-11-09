# api-lab

Link: https://github.com/AlanT011/api-lab.git

## Input Domain Model for POST /api/ratings

A valid request requires an integer number of stars from 1 to 5,
an existing pizza, and a logged-in user's token.

| Characteristic | Blocks | Test values |
|---|---|---|
| C1: Value of stars | Below 1; 1 to 5 (base); above 5 | 0; 3; 6 |
| C2: Type of stars | Integer (base); decimal; text; missing | 3; 3.5; "3"; no stars field |
| C3: Pizza | Exists (base); does not exist | A generated pizza ID; 999999999 |
| C4: Token | User's own (base); none; wrong length | Login token; no header; token short |

The base choice uses 3 integer stars, an existing pizza,
and the user's own token.

Each additional test changes one characteristic from the base
while keeping the others at their base choices.

### Test coverage

| Characteristic | Block | Test |
|---|---|---|
| C1: Value of stars | Below 1 | test_stars_out_of_range[0] |
| C1: Value of stars | 1 to 5 (base) | test_base_choice_is_saved |
| C1: Value of stars | Above 5 | test_stars_out_of_range[6] |
| C2: Type of stars | Integer (base) | test_base_choice_is_saved |
| C2: Type of stars | Decimal | test_invalid_stars_type[decimal] |
| C2: Type of stars | Text | test_invalid_stars_type[text] |
| C2: Type of stars | Missing | test_invalid_stars_type[missing] |
| C3: Pizza | Exists (base) | test_base_choice_is_saved |
| C3: Pizza | Does not exist | test_nonexistent_pizza_is_refused |
| C4: Token | User's own (base) | test_base_choice_is_saved |
| C4: Token | None | test_missing_token_is_refused |
| C4: Token | Wrong length | test_short_token_is_refused |

Base choice coverage requires:
1 + (3 - 1) + (4 - 1) + (2 - 1) + (3 - 1) = 9 tests.

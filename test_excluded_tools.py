import pytest


# A recommended pizza never uses an excluded tool.
# @pytest.mark.parametrize("excluded", [["Knife"], ["Scissors"]])
# def test_excluded_tool_is_not_used(api, auth, excluded):
#     res = api.post(
#         "/api/pizza",
#         json={"excludedTools": excluded},
#         headers=auth,
#     )

#     assert res.status_code == 200
#     assert res.json()["pizza"]["tool"] not in excluded

# @pytest.mark.parametrize(
#     "excluded",
#     [
#         [],
#         ["Knife"],
#         ["Scissors"],
#         ["Knife", "Scissors"],
#         ["Knife", "Pizza cutter", "Scissors"],
#     ],
# )
import pytest


# A satisfiable request never returns an excluded tool.
@pytest.mark.parametrize(
    "excluded",
    [
        [],
        ["Knife"],
        ["Scissors"],
        ["Knife", "Scissors"],
    ],
)
def test_excluded_tool_is_not_used(api, auth, excluded):
    res = api.post(
        "/api/pizza",
        json={"excludedTools": excluded},
        headers=auth,
    )

    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


# An impossible restriction should return 400 and a JSON error.
@pytest.mark.xfail(
    reason="Defect 1: excluding all tools returns 500 with an empty body",
    strict=True,
)
def test_excluding_all_tools_is_refused(api, auth):
    res = api.post(
        "/api/pizza",
        json={
            "excludedTools": ["Knife", "Pizza cutter", "Scissors"]
        },
        headers=auth,
    )

    assert res.status_code == 400

    body = res.json()
    assert isinstance(body, dict)
    assert isinstance(body.get("error"), str)
    assert body["error"].strip()
    
type Account = dict[str, str|int] | None
type Accounts = list[Account] | None
type User = dict[str, str|Accounts] | None
type Users = list[User] 
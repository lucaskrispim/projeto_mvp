# Endpoints do WebServices

## Rotas GET
### Conta do usuário
```http
GET /users/user/account
```
| Parameter  | Type      |
| :--------- | :-------- |
| `name`     | `string`  |
| `email`    | `string`  |
| `password`      | `integer` |


## Rotas POST
### Criação de conta
```http
POST /users/user/signup
```
| Parameter  | Type      |
| :--------- | :-------- |
| `name`     | `string`  |
| `email`    | `string`  |
| `password`      | `integer` |
| `address`      | `string` |
| `city`      | `string` |


### Login do usuário
```http
POST /users/user/login
```
| Parameter  | Type      |
| :--------- | :-------- |
| `name`     | `string`  |
| `email`    | `string`  |
| `password`      | `integer` |

### Autenticação
```http
POST /users/user/auth
```
| Parameter  | Type      |
| :--------- | :-------- |
| `token`     | `string`  |



### Definir plano de assinatura
```http
POST /users/user/plan
```
| Parameter  | Type      |
| :--------- | :-------- |
| `plan_type`     | `string`  |

### Pagamentos
```http
POST /users/user/checkout
```
| Parameter  | Type      |
| :--------- | :-------- |
| `name`     | `string`  |
| `email`    | `string`  |
| `password`      | `integer` |

### Salvar cartão
```http
POST /users/user/credit_card
```
| Parameter  | Type      |
| :--------- | :-------- |
| `cvv`     | `integer`  |
| `card_numbers`    | `integer`  |
| `expiration`      | `integer` |
| `recurring_payment`      | `boolean` |


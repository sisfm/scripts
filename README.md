# Shopping Basket

Python Script for Lana challenge which simulate a shopping cart
## Download
```
mkdir shopping_cart
cd shopping_cart
git clone https://github.com/sisfm/scripts.git .
```
## Build

```
docker build -t shopping_cart .
```
## Unit Test
```
python -m unittest -v #Part of Dockerfile
```

## Execution

```
docker run -it --rm --name shopping_cart shopping_cart
```

## Main Menu

```
*****************************************MENU*******************************************
1.Display Stock
2.Add Item to Basket
3.Remove Item From Basket
4.Display Basket
5.Checkout
6.Empty Basket
****************************************************************************************
```

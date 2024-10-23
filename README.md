# rest_ordering_with_AI

## Logic for Chart GPT
objectives:
    take an order
    handle money transaction

    Take an Order
        inputs:
            order number


        logic
            collect the orders
            find the price for each of the order
            calculate the sum for the order
            return the value for the sum of the order

        output:
            display the sum of the order



    Handle Money Transactions
        input:
            money paid for the order

        logic:
            calculate the change due
            generate an order number
            generate a receipt number

        output:
            display the following
                each order description
                cost for each order
                total cost of the order
                amount of money paid for the order
                amount of change due
                oder number
                receipt number


## Data Model for Order Object
    Data Model for 1 order object
        {
            1:{
                'order_name': 'cheese burger meal',
                'order_desc': 'cheese burger - fries - medium drink',
                'order_price: 5.34
            }
        }

    Data Model for all oder objects
        {
            'all_orders': [
                {
                    1:{
                        'order_name': 'cheese burger meal',
                        'order_desc': 'cheese burger - fries - medium drink',
                        'order_price: 5.34
                    }
                },
                {
                    2:{
                        'order_name': 'dark chicken meal',
                        'order_desc': '1/4 dark chicken - fries - medium drink',
                        'order_price: 11.49
                    }
                },
                {
                    3:{
                        'order_name': 'white chicken meal',
                        'order_desc': '1/4 white chicken - fries - medium drink',
                        'order_price: 21.49
                    }
                }

            ]
        }



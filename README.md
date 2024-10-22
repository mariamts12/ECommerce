## E-commerce Website

This project is a basic e-commerce web application using Django. The project includes several HTML templates for key pages, CSS, and JavaScript files located in the `static` folder, as well as Django models for products, categories, carts, and cart items. This initial version of the application focuses on setting up the frontend and basic structure for future functionality.

---

## Pages

1. **Home Page ("/")**:
   - Displays store products, bestsellers etc.
   
2. **Listing Page ("/category/<slug:slug>/")**:
   - Lists all products under a selected category with filters.
   
3. **Product Detail Page ("/product/<slug:slug>/")**:
   - Shows details of a specific product (e.g., description, price, etc.).

4. **Cart Page ("/order/cart/")**:
   - Shows the user's cart items, allowing them to review their selections.
   
5. **Checkout Page ("/order/checkout/")**:
   - A form for completing the order.
   
6. **Contact Page ("/contact/")**:
   - A basic contact form.
# django-eCommerce-template

Welcome to the Django E-Commerce Template Project! This project is a starting point for building an e-commerce website using Django.

### Features

* Admin user can list products with descriptions, prices, and images
* Users can sign up and add items to a wishlist
* Search functionality to find products
* Admin user can add blog posts

### Prerequisites

* Python 3.8.1 or higher
* Django 4.0.3 or higher

### Getting Started

1. Clone the repository:

``` git clone https://github.com/raw0ol/django-eCommerce-template.git ```

2. Change into the project directory:

``` cd django-ecommerce-template ```

3. A virtual environment: It is recommended to set up a virtual environment for your Django project to keep its dependencies separate from other Python projects on your system. You can create a virtual environment using the venv module that comes with Python 3.8.1 or higher.

4. Install the required packages:

```pip install -r requirements.txt ```

5. Run the migrations to create the database tables:

``` python manage.py migrate ```

6. Create a superuser to access the admin panel:

``` python manage.py createsuperuser ```

7. Run the development server:

``` python manage.py runserver ```

8. Open your web browser and navigate to http://127.0.0.1:8000/ to see the site.

### Adding Products

1. Log in to the admin panel at http://127.0.0.1:8000/admin/
2. Click on the "Products" link in the "APP_STORE" section
3. Click on the "Add Product" button
4. Enter the product information and click "Save" (feature items appear in homepage)

### Adding to Wishlist

1. Sign up for an account at http://127.0.0.1:8000/accounts/register/
2. Log in to your account
3. Browse the products and click the "Add to Wishlist" button for any products you want to save
4. To view your wishlist, go to account profile at http://127.0.0.1:8000/accounts/profile/ and click on the "See All" link in the top right corner of the profile

### Searching for Products

Use the search box in the top menu to search for products by name.

### Blog Post

1. Log in to the admin panel at http://127.0.0.1:8000/admin/
2. Click on the "Blogs" link in the "APP_BLOG" section
3. Click on the "Add Blog" button
4. Enter the blog information and click "Save"
5. To add sections to blog post, navigate back to the admin panel and click on the "Blog Sections" section in the left-hand menu.
6. Click on the "Add Blog Section" button at the top right of the page.
7. Enter the blog section information and select which Blog to add this section to.

You should now be able to view your new blog post on the front-end of your Django website.

### Disclaimer

This project is for educational purposes only and is not intended for use in a production environment. No buying functionality has been implemented.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
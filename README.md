# django-bootstrapCRUD-cw

Create a garage sell site that will help people sell their old garbage. The index page should have a form to add a new item, then show all items for sale. Each item should include a picture URL, name, description, and price. Use a Bootstrap Card to make each item look good. once an item is created it should be automatically added to the home page.

<strong>Challenge: </strong>
Add a CSS Grid to this page so you can have multiple items per row.

Bootstrap card can be found here: https://getbootstrap.com/docs/4.0/components/card/
<hr>
1.5 points. The blank form is ovewritting the request.POST form every time, even in the POST request. If you want it blank it should only be in the GET request.
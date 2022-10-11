const BASE_URL = "https://jsonplaceholder.typicode.com";
const POSTS_URL = "posts/";

const listaDePosts = $("#lista-posts");

$.get(BASE_URL + "/" + POSTS_URL, function (data) {
  for (item of data) {
    const newLi = $("<li></li>").text(item.title);
    newLi.css({ cursor: "pointer", "margin-top": "10px" });

    const content = $("<p>" + item.body + "</p>");
    content.css("display", "none");
    content.css("background-color", "lightgray");

    newLi.append(content);

    newLi.click(function () {
      content.slideToggle();
    });

    listaDePosts.append(newLi);
  }
});

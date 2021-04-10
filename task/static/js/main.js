$(document).ready(function () {
  $(".modalOpenButton").on("click", function () {
    let modal = $(this).next(".modal");
    modal.css("display", "block");
    $(modal)
      .find(".close")
      .on("click", function () {
        modal.css("display", "none");
      });
  });
});

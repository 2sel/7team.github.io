$(document).ready(function () {
  show_templates();
});

function show_templates() {
  $.ajax({
    type: "GET",
    url: "/templates",
    data: {},
    success: function (response) {
      console.log("성공");
      let rows = response["comments"];
      for (let i = 0; i < rows.length; i++) {
        let name = rows[i]["name"];
        let comment = rows[i]["comment"];
        let num = rows[i]["num"];
        let done = rows[i]["done"];

        let temp_html = ``;
        if (done == 0) {
          temp_html = `
                                  <h4>😊 ${name}</h4>
                                  <p>${comment}</p>
                                  <button onclick="done_templates(${num})" type="button" class="btn btn-outline-primary">댓글 지우기</button>
                              `;
        }
        $("#comment_list").append(temp_html);
      }
    },
  });
}

function save_templates() {
  let name = $("#name").val();
  let comment = $("#comment").val();

  $.ajax({
    type: "POST",
    url: "/templates",
    data: { name_give: name, comment_give: comment },
    success: function (response) {
      alert(response["msg"]);
      window.location.reload();
    },
  });
}
function done_templates(num) {
  $.ajax({
    type: "POST",
    url: "/templates/done",
    data: { num_give: num },
    success: function (response) {
      alert(response["msg"]);
      window.location.reload();
    },
  });
}

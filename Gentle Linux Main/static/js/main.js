// Main application script for support Marked
  $(document).ready(function(){
    $(".detail-text").each(function(){
      var content = $(this).text()
      console.log(content)
      var markdown = marked(content)
      console.log(markdown)
      $(this).html(markdown)
    })
      $("#detail").each(function () {
          $(this).addClass("img-responsive")
      })
  })

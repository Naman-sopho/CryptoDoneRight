document.write('<script type="text/javascript" src="js/links.js"></script>');
 window.onload = function()
 {
	document.querySelector('#search').addEventListener('click',Search);
	 document.addEventListener('keypress', function(event) {
            if (event.keyCode === 13 || event.which === 13) {
                Search();
            }
        });
 }

  var searcher = function(req) {
  		 
  		for(i=0; i<links.length;i++)
  		{
  			if(links[i].name.toLowerCase().trim() == req.toLowerCase().trim())
  			{
  				return links[i].link;
  				break;
  			}
  		}
  }

  function Search()
  {
  	var searchKeyword = document.getElementById('txt_search').value;
  	window.location = searcher(searchKeyword);
  }


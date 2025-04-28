// Using D3.js to query Solr
d3.json("http://localhost:8983/solr/assignment3/select?q=*:*&rows=1000", function(error, data) {
    if (error) throw error;
    var documents = data.response.docs;
    console.log(documents);
      // Can now visualize "documents" however you want
  });
  

// d3.json("http://localhost:8983/solr/assignment3/select?q=*:*", function(error, data) {
//   if (error) throw error;
//   var documents = data.response.docs;
//   // Do something with the parsed data
// });
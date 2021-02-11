/* function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
} */

function deleteAsset(portfolioId) {
    fetch("/delete-asset", {
      method: "POST",
      body: JSON.stringify({ portfolioId: portfolioId })
    }).then((_res) => {
      window.location.href = "/";
    });
}

# 🎥 Latest YouTube Videos

Below are the most recent videos from the [Let's Patch Your System](https://www.youtube.com/@LetsPatchYourSystem) channel.

<div id="yt-videos"></div>

<script>
async function loadVideos() {
  const channelId = "UC"; // TODO: replace with your channel ID
  const response = await fetch("https://www.youtube.com/feeds/videos.xml?channel_id=" + channelId);
  const text = await response.text();
  const parser = new DOMParser();
  const xml = parser.parseFromString(text, "application/xml");
  const entries = xml.getElementsByTagName("entry");
  
  let html = '<ul>';
  for (let i = 0; i < Math.min(entries.length, 5); i++) {
    const title = entries[i].getElementsByTagName("title")[0].textContent;
    const link = entries[i].getElementsByTagName("link")[0].getAttribute("href");
    const published = entries[i].getElementsByTagName("published")[0].textContent.split("T")[0];
    html += `<li><a href="${link}" target="_blank">${title}</a> <small>(${published})</small></li>`;
  }
  html += '</ul>';
  document.getElementById("yt-videos").innerHTML = html;
}

loadVideos();
</script>

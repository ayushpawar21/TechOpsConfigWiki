# 🎥 Latest YouTube Videos

Welcome to the **Let's Patch Your System** YouTube dashboard!  
This page automatically fetches and displays the most recent uploads from the channel.  
No API key or manual updates needed 🚀

<div id="yt-videos" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem;"></div>

<script>
async function getChannelIdFromHandle(handle) {
  try {
    const html = await fetch(`https://www.youtube.com/${handle}`).then(r => r.text());
    const match = html.match(/"channelId":"(UC[\\w-]+)"/);
    return match ? match[1] : null;
  } catch (e) {
    console.error("Failed to fetch channel ID:", e);
    return null;
  }
}

async function loadVideos() {
  const handle = "@LetsPatchYourSystem";
  const container = document.getElementById("yt-videos");
  container.innerHTML = "<p>Loading latest videos...</p>";

  const channelId = await getChannelIdFromHandle(handle);
  if (!channelId) {
    container.innerHTML = "<p>⚠️ Unable to fetch channel data. Please check the handle.</p>";
    return;
  }

  try {
    const feedUrl = `https://www.youtube.com/feeds/videos.xml?channel_id=${channelId}`;
    const response = await fetch(feedUrl);
    const text = await response.text();
    const parser = new DOMParser();
    const xml = parser.parseFromString(text, "application/xml");
    const entries = xml.getElementsByTagName("entry");

    if (entries.length === 0) {
      container.innerHTML = "<p>No videos found yet.</p>";
      return;
    }

    let html = "";
    for (let i = 0; i < Math.min(entries.length, 6); i++) {
      const title = entries[i].getElementsByTagName("title")[0].textContent;
      const link = entries[i].getElementsByTagName("link")[0].getAttribute("href");
      const videoId = link.split("v=")[1];
      const published = entries[i].getElementsByTagName("published")[0].textContent.split("T")[0];

      html += `
        <div style="border: 1px solid #ccc; border-radius: 10px; overflow: hidden; background: #fafafa; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
          <iframe width="100%" height="200" src="https://www.youtube.com/embed/${videoId}" frameborder="0" allowfullscreen></iframe>
          <div style="padding: 10px;">
            <strong>${title}</strong><br>
            <small>📅 ${published}</small><br>
            <a href="${link}" target="_blank">🔗 Watch on YouTube</a>
          </div>
        </div>
      `;
    }

    container.innerHTML = html;
  } catch (error) {
    console.error("Error loading videos:", error);
    container.innerHTML = "<p>⚠️ Failed to load videos. Please try again later.</p>";
  }
}

loadVideos();
</script>

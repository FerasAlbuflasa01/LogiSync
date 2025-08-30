// Initialize and add the map
let map
let userMarker
async function initMap(position) {
  const { Map } = await google.maps.importLibrary('maps')
  const { AdvancedMarkerElement } = await google.maps.importLibrary('marker')

  //init map
  map = new Map(document.getElementById('map'), {
    zoom: 17,
    center: { lat: -34.397, lng: 150.644 },
    mapId: 'DEMO_MAP_ID'
  })

  setInterval(() => {
    navigator.geolocation.getCurrentPosition((pos) => {
      let position = {
        lat: pos.coords.latitude,
        lng: pos.coords.longitude
      }
      
      if(pos.coords.accuracy>=200){
        map.setCenter(position)

      // The marker, positioned at Uluru
      if (!userMarker) {
        userMarker = new google.maps.Marker({
          position: position,
          map: map,
          title: 'You are here!'
        })
      } else {
        // Move the existing marker to the new position
        userMarker.setPosition(position)
      }
      }
      
    })
  }, 5000)

  // The map, centered at Uluru
}

// const getUserLocation = () => {
//   navigator.geolocation.watchPosition((pos) => {
//     let position = {
//       lat: pos.coords.latitude,
//       lng: pos.coords.longitude
//     }
//     console.log(pos)

//     initMap(position)
//   })
// }
initMap()
//setInterval(initMap,1000)

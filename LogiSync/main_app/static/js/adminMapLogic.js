// Initialize and add the map
let map
let userMarker
const url = new URL(window.location.href)
const pathSegments = url.pathname.split('/')
const containerId = pathSegments[3]
const initMap = async () => {
  const response = await getLocation()
  const { Map } = await google.maps.importLibrary('maps')
  const { AdvancedMarkerElement } = await google.maps.importLibrary('marker')
  //init map
  let position
  if (response.data.status !== 'faild') {
    position = {
      lat: response.data.lat,
      lng: response.data.lng
    }
  } else {
    position = { lat: -34.397, lng: 150.644 }
  }
  map = new Map(document.getElementById('map'), {
    zoom: 17,
    center: position,
    mapId: 'DEMO_MAP_ID'
  })
  userMarker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: 'Uluru'
  })

  setInterval(async() => {
    let response = await getLocation()
    navigator.geolocation.getCurrentPosition
    position = {
      lat: response.data.lat,
      lng: response.data.lng
    }

    // The marker, positioned at Uluru

    // Move the existing marker to the new position
    userMarker.position = position
  }, 5000)

  // The map, centered at Uluru
}
const getLocation = async () => {
  return await axios.post('http://127.0.0.1:8000/location/load', {
    id: containerId
  })
}
initMap()

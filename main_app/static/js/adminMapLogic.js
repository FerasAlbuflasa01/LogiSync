// Initialize and add the map
let map
let userMarker
const baseUrl= 'https://logisync-eadf6892bb3a.herokuapp.com/'
const url = new URL(window.location.href)
const pathSegments = url.pathname.split('/')
const transportId = pathSegments[2]
const error = (err) => {
  console.error(`ERROR(${err.code}): ${err.message}`)
}
const initMap = async () => {
  const response = await axios.post(`${baseUrl}location/load`, {
    id: transportId
  })

  const { Map } = await google.maps.importLibrary('maps')
  const { AdvancedMarkerElement } = await google.maps.importLibrary('marker')

  //init map
  let position
  if (response.data.status !== 'faild') {
    position = {
      lat: response.data.lat,
      lng: response.data.lng,
      id: transportId
    }
  } else {
    position = { lat: -34.397, lng: 150.644 }
  }

  map = new Map(document.getElementById('map'), {
    zoom: 17,
    center: position,
    mapId: 'DEMO_MAP_ID'
  })

  //get route

  const encodedPoline = await getRoute(
    response.data.origin,
    response.data.destination
  )
  let path = google.maps.geometry.encoding.decodePath(
    encodedPoline.data.routes[0].polyline.encodedPolyline
  )

  //add path  to map

  const polyline = new google.maps.Polyline({
    path: path,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  })
  polyline.setMap(map)

  const userMarker = new AdvancedMarkerElement({
    map: map,
    position: position,

    title: 'Uluru'
  })

  const startMarker = new google.maps.Marker({
    position: path[0],
    map: map,
    title: 'start point'
  })
  const endMarker = new google.maps.Marker({
    position: path[path.length - 1],
    map: map,
    title: 'End point'
  })

  setInterval(async () => {
    const response = await axios.post(`${baseUrl}location/load`, {
      id: transportId
    })
      let position = {
      lat: response.data.lat,
      lng: response.data.lng,
      id: transportId
    }
    if (pos.coords.accuracy > 80) {
      map.setCenter(position)

      // The marker, positioned at Uluru
      if (!userMarker) {
        userMarker = new AdvancedMarkerElement({
          map: map,
          position: position,
          title: 'Uluru'
        })
      } else {
        // Move the existing marker to the
        userMarker.position = position
      }
    }
  }, 5000)

  // The map, centered at Uluru
}

const getRoute = async (origin, destination) => {
  return await axios.post(
    'https://routes.googleapis.com/directions/v2:computeRoutes',
    {
      origin: {
        address: origin
      },
      destination: {
        address: destination
      },
      travelMode: 'DRIVE'
    },
    {
      headers: {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': 'AIzaSyCaHQPAnFHmdGi19QlEmBuJ5iuaNkmPuwI',
        'X-Goog-FieldMask':
          'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'
      }
    }
  )
}

initMap()

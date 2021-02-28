export default function getLastSegUrl() {
    return location.pathname.split("/").pop()
}
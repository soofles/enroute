import "./StopItem.css"
import type { Stop } from "../types/Stop"
import { formatDateTime } from "../utils/FormatDateTime";

interface StopProps {
    stop: Stop;
}

export default function StopItem({ stop }: StopProps) {
    return (
        <div className="stop-item">
            <h3>{stop.name}</h3>
            <span>{stop.address}</span>
            <span>${stop.cost}</span>
            <span>{formatDateTime(stop.arrival_time)} - {formatDateTime(stop.departure_time)}</span>
        </div>
    )
}
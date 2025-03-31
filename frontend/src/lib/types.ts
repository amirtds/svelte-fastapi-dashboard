export interface SensorReading {
  timestamp: string;
  temperature: number;
  humidity: number;
  status: 'normal' | 'warning' | 'critical';
}
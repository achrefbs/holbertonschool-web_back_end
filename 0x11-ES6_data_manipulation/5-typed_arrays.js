export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  if (position >= length) {
    throw Error('Position outside range');
  }
  return new DataView(buffer).setInt8(position, value);
}

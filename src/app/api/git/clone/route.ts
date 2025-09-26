import { NextRequest, NextResponse } from 'next/server';

const TARGET_SERVER_BASE_URL = process.env.SERVER_BASE_URL || 'http://localhost:8001';

export async function POST(request: NextRequest) {
  try {
    // Get the request body
    const body = await request.json();
    
    // Forward the request to the backend API
    const response = await fetch(`${TARGET_SERVER_BASE_URL}/git/clone`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body)
    });

    // Get the response data
    const data = await response.text();

    // Return the response with the same status code
    return new NextResponse(data, {
      status: response.status,
      headers: {
        'Content-Type': response.headers.get('Content-Type') || 'application/json',
      },
    });

  } catch (error) {
    console.error('Error forwarding request to backend:', error);
    return NextResponse.json(
      { error: 'Failed to forward request to backend' },
      { status: 500 }
    );
  }
}

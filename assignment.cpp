#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Point {
    int x, y;
};

struct Segment {
    Point p1, p2;
};

int orientation(Point a, Point b, Point c) {
    int val = (b.y - a.y)*(c.x - b.x) - (b.x - a.x)*(c.y - b.y);
    if (val == 0) return 0;     // colinear
    return (val > 0) ? 1 : 2;   // clock or counterclock wise
}

bool onSegment(Point p, Point q, Point r) {
    return q.x <= max(p.x, r.x) && q.x >= min(p.x, r.x) &&
           q.y <= max(p.y, r.y) && q.y >= min(p.y, r.y);
}

bool doIntersect(Point p1, Point q1, Point p2, Point q2) {
    int o1 = orientation(p1, q1, p2);
    int o2 = orientation(p1, q1, q2);
    int o3 = orientation(p2, q2, p1);
    int o4 = orientation(p2, q2, q1);

    if (o1 != o2 && o3 != o4) return true;
    if (o1 == 0 && onSegment(p1, p2, q1)) return true;
    if (o2 == 0 && onSegment(p1, q2, q1)) return true;
    if (o3 == 0 && onSegment(p2, p1, q2)) return true;
    if (o4 == 0 && onSegment(p2, q1, q2)) return true;
    return false;
}

Point pivot;
bool cmp(Point a, Point b) {
    int dx1 = a.x - pivot.x, dy1 = a.y - pivot.y;
    int dx2 = b.x - pivot.x, dy2 = b.y - pivot.y;
    return dy1 * dx2 < dy2 * dx1;
}

vector<Point> convexHull(vector<Point>& points) {
    int n = points.size(), pivotIndex = 0;
    for (int i = 1; i < n; ++i)
        if (points[i].y < points[pivotIndex].y || 
           (points[i].y == points[pivotIndex].y && points[i].x < points[pivotIndex].x))
            pivotIndex = i;
    swap(points[0], points[pivotIndex]);
    pivot = points[0];

    sort(points.begin() + 1, points.end(), cmp);
    vector<Point> hull;
    for (Point pt : points) {
        while (hull.size() >= 2 &&
               orientation(hull[hull.size()-2], hull[hull.size()-1], pt) != 2)
            hull.pop_back();
        hull.push_back(pt);
    }
    return hull;
}

int main() {
    vector<Segment> segments = {
        {{1, 1}, {4, 4}},
        {{1, 4}, {4, 1}},
        {{2, 2}, {6, 2}},
        {{3, 1}, {3, 5}}
    };

    cout << "Segment Intersections:\n";
    for (int i = 0; i < segments.size(); ++i) {
        for (int j = i + 1; j < segments.size(); ++j) {
            if (doIntersect(segments[i].p1, segments[i].p2,
                            segments[j].p1, segments[j].p2)) {
                cout << "Segment " << i+1 << " intersects with Segment " << j+1 << "\n";
            }
        }
    }

    vector<Point> allPoints;
    for (auto seg : segments) {
        allPoints.push_back(seg.p1);
        allPoints.push_back(seg.p2);
    }

    vector<Point> hull = convexHull(allPoints);
    cout << "\nConvex Hull:\n";
    for (auto p : hull)
        cout << "(" << p.x << ", " << p.y << ")\n";

    return 0;
}

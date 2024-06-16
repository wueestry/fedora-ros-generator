# Meta Package
Name:           ros-iron-tf2
Version:        0.31.7
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/tf2
Summary:        Meta package for ros2-iron-tf2 and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tf2
Requires:       ros2-iron-tf2-devel

Obsoletes: ros-iron-tf2 < 0.31.7-1

%description
tf2 is the second generation of the transform library, which lets the
user keep track of multiple coordinate frames over time. tf2 maintains
the relationship between coordinate frames in a tree structure
buffered in time, and lets the user transform points, vectors, etc
between any two coordinate frames at any desired point in time.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.7-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.31.6-1
- Update to latest release

# Meta Package
Name:           ros-jazzy-stomp
Version:        0.1.2
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://wiki.ros.org/stomp
Summary:        Meta package for ros2-jazzy-stomp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-stomp
Requires:       ros2-jazzy-stomp-devel

Obsoletes: ros-jazzy-stomp < 0.1.2-1

%description
This package provides the STOMP (Stochastic Trajectory Optimization
for Motion Planning) algorithm that can be used for robot motion
planning tasks or other similar optimization tasks

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.1.2-1
- Update to latest release

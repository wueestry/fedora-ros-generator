# Meta Package
Name:           ros-jazzy-vision-msgs
Version:        4.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-vision_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-vision_msgs
Requires:       ros2-jazzy-vision_msgs-devel

Obsoletes: ros-jazzy-vision-msgs < 4.1.1-1

%description
Messages for interfacing with various computer vision pipelines, such
as object detectors.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.1-1
- Update to latest release

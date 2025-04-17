# Meta Package
Name:           ros-jazzy-stereo-msgs
Version:        5.3.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-stereo_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-stereo_msgs
Requires:       ros2-jazzy-stereo_msgs-devel

Obsoletes: ros-jazzy-stereo-msgs < 5.3.6-1

%description
A package containing some stereo camera related message definitions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.6-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.3.5-1
- Update to latest release

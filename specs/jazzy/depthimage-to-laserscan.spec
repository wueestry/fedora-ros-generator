# Meta Package
Name:           ros-jazzy-depthimage-to-laserscan
Version:        2.5.1
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/depthimage_to_laserscan
Summary:        Meta package for ros2-jazzy-depthimage_to_laserscan and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-depthimage_to_laserscan
Requires:       ros2-jazzy-depthimage_to_laserscan-devel

Obsoletes: ros-jazzy-depthimage-to-laserscan < 2.5.1-1

%description
depthimage_to_laserscan

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.5.1-1
- Update to latest release

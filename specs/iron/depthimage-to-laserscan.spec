# Meta Package
Name:           ros-iron-depthimage-to-laserscan
Version:        2.5.1
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/depthimage_to_laserscan
Summary:        Meta package for ros2-iron-depthimage_to_laserscan and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-depthimage_to_laserscan
Requires:       ros2-iron-depthimage_to_laserscan-devel

Obsoletes: ros-iron-depthimage-to-laserscan < 2.5.1-1

%description
depthimage_to_laserscan

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.5.1-1
- Update to latest release

# Meta Package
Name:           ros-jazzy-rviz-common
Version:        14.1.0
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/ros2/rviz/blob/ros2/README.md
Summary:        Meta package for ros2-jazzy-rviz_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_common
Requires:       ros2-jazzy-rviz_common-devel

Obsoletes: ros-jazzy-rviz-common < 14.1.0-1

%description
Common rviz API, used by rviz plugins and applications.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release

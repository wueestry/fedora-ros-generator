# Meta Package
Name:           ros-jazzy-rviz-default-plugins
Version:        14.1.0
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/ros2/rviz/blob/ros2/README.md
Summary:        Meta package for ros2-jazzy-rviz_default_plugins and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_default_plugins
Requires:       ros2-jazzy-rviz_default_plugins-devel

Obsoletes: ros-jazzy-rviz-default-plugins < 14.1.0-1

%description
Several default plugins for rviz to cover the basic functionality.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release

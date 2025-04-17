# Meta Package
Name:           ros-jazzy-pal-statistics-msgs
Version:        2.6.2
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/pal-robotics/pal_statistics
Summary:        Meta package for ros2-jazzy-pal_statistics_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pal_statistics_msgs
Requires:       ros2-jazzy-pal_statistics_msgs-devel

Obsoletes: ros-jazzy-pal-statistics-msgs < 2.6.2-1

%description
Statistics msgs package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.2-1
- Update to latest release

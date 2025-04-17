# Meta Package
Name:           ros-jazzy-pal-statistics
Version:        2.6.2
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/pal-robotics/pal_statistics
Summary:        Meta package for ros2-jazzy-pal_statistics and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pal_statistics
Requires:       ros2-jazzy-pal_statistics-devel

Obsoletes: ros-jazzy-pal-statistics < 2.6.2-1

%description
The pal_statistics package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.6.2-1
- Update to latest release

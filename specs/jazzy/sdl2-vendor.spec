# Meta Package
Name:           ros-jazzy-sdl2-vendor
Version:        3.3.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-sdl2_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-sdl2_vendor
Requires:       ros2-jazzy-sdl2_vendor-devel

Obsoletes: ros-jazzy-sdl2-vendor < 3.3.0-1

%description
Vendor library for SDL2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.3.0-1
- Update to latest release

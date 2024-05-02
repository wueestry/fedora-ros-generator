# Meta Package
Name:           ros-jazzy-mimick-vendor
Version:        0.6.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/Snaipe/Mimick
Summary:        Meta package for ros2-jazzy-mimick_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-mimick_vendor
Requires:       ros2-jazzy-mimick_vendor-devel

Obsoletes: ros-jazzy-mimick-vendor < 0.6.1-1

%description
Wrapper around mimick, it provides an ExternalProject build of mimick.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.6.1-1
- Update to latest release
